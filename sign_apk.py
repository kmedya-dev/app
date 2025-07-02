import subprocess
import os
import sys

def sign_and_align_apk(apk_path, keystore_path, alias, keystore_password, key_password):
    # 1. Sign the APK using jarsigner
    print(f"Signing APK: {apk_path}")
    jarsigner_command = [
        "jarsigner",
        "-verbose",
        "-sigalg", "SHA256withRSA",
        "-digestalg", "SHA-256",
        "-keystore", keystore_path,
        "-storepass", keystore_password,
        "-keypass", key_password,
        apk_path,
        alias
    ]
    try:
        subprocess.run(jarsigner_command, check=True, capture_output=True, text=True)
        print("APK signed successfully with jarsigner.")
    except subprocess.CalledProcessError as e:
        print(f"Error signing APK with jarsigner: {e}")
        print(f"Stdout: {e.stdout}")
        print(f"Stderr: {e.stderr}")
        sys.exit(1)

    # 2. Find zipalign
    zipalign_path = None
    android_home = os.environ.get('ANDROID_HOME')
    if android_home:
        # Search in common build-tools locations
        for root, dirs, files in os.walk(os.path.join(android_home, 'build-tools')):
            if 'zipalign' in files:
                zipalign_path = os.path.join(root, 'zipalign')
                break
    
    # Fallback for Termux android-tools installation
    if not zipalign_path:
        try:
            # Check if zipalign is directly in PATH (e.g., from pkg install android-tools)
            subprocess.run(["which", "zipalign"], check=True, capture_output=True, text=True)
            zipalign_path = "zipalign"
        except subprocess.CalledProcessError:
            print("zipalign not found in ANDROID_HOME or PATH. Please ensure Android SDK Build Tools or android-tools are installed and configured.")
            sys.exit(1)

    # 3. Align the APK using zipalign
    aligned_apk_path = apk_path.replace("-unsigned.apk", "-signed-aligned.apk").replace(".apk", "-aligned.apk")
    print(f"Aligning APK to: {aligned_apk_path}")
    zipalign_command = [
        zipalign_path,
        "-v", "4",
        apk_path,
        aligned_apk_path
    ]
    try:
        subprocess.run(zipalign_command, check=True, capture_output=True, text=True)
        print("APK aligned successfully with zipalign.")
        print(f"Final signed and aligned APK: {aligned_apk_path}")
    except subprocess.CalledProcessError as e:
        print(f"Error aligning APK with zipalign: {e}")
        print(f"Stdout: {e.stdout}")
        print(f"Stderr: {e.stderr}")
        sys.exit(1)

    # Optionally, replace the original unsigned APK with the signed and aligned one
    # os.replace(aligned_apk_path, apk_path)
    # print(f"Replaced original APK with signed and aligned version: {apk_path}")

if __name__ == "__main__":
    if len(sys.argv) != 6:
        print("Usage: python sign_apk.py <apk_path> <keystore_path> <alias> <keystore_password> <key_password>")
        sys.exit(1)

    apk_file = sys.argv[1]
    keystore_file = sys.argv[2]
    key_alias = sys.argv[3]
    ks_pass = sys.argv[4]
    key_pass = sys.argv[5]

    sign_and_align_apk(apk_file, keystore_file, key_alias, ks_pass, key_pass)
