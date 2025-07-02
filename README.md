# Eruda Browser

This project is a simple Android browser that injects the [Eruda](https://github.com/liriliri/eruda) developer console into every webpage. It's built using [Apache Cordova](https://cordova.apache.org/) and can be built and signed automatically using GitHub Actions.

## ✨ Features

*   **Lightweight Android Browser:** A minimal webview-based browser.
*   **Developer Console:** Eruda is injected on every page, providing a powerful console for debugging, inspecting elements, and monitoring network requests.
*   **Automated Builds:** The included GitHub Actions workflow automatically builds, signs, and uploads a release-ready APK on every push to `main`.

## 🚀 How to Use Eruda

Eruda is automatically injected into every webpage. To open the Eruda console, simply tap the screen three times quickly. You can then use its various features for debugging and inspection.

## 📂 Project Structure

```
.
├── .github/
│   └── workflows/
│       └── build.yml       # GitHub Actions workflow for automated builds
├── www/
│   ├── index.html          # Main HTML file for the browser's webview
│   └── eruda.min.js        # Eruda console library, injected into webpages
├── build.py                # Python script with build variables
├── update_config.py        # Python script to update Cordova's config.xml
├── icon.png                # Application icon
├── release.keystore        # Keystore for signing the APK
└── README.md               # This file
```

## 🛠️ Technologies Used

*   **[Apache Cordova](https://cordova.apache.org/):** For creating the Android application from web assets.
*   **[GitHub Actions](https://github.com/features/actions):** For CI/CD and automated builds.
*   **[Python](https://www.python.org/):** Used for build scripts and configuration management.
*   **[Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/):** For parsing and modifying `config.xml` during the build process.

## 🚀 Getting Started

This project is set up for automated builds via GitHub Actions. To get a signed APK, simply push a commit to the `main` branch. The workflow will run, and a signed APK will be available as a downloadable artifact.

### Manual Build (Local)

If you want to build the project locally, you will need:

*   [Node.js](https://nodejs.org/) (v18+)
*   [Cordova CLI](https://cordova.apache.org/docs/en/latest/guide/cli/) (`npm install -g cordova`)
*   [Python](https://www.python.org/) (v3+)
*   Android SDK

Once you have the prerequisites, you can run the following commands:

```bash
# Install Python dependencies
pip install beautifulsoup4 lxml

# Navigate to the Cordova project directory
cd cordova_project

# Add the Android platform (if not already added)
cordova platform add android

# Copy web assets from the root www/ directory to the Cordova project's www/ directory
cp -r ../www/* www/

# Build the APK
cordova build android --release
```

## 🔐 Signing

The GitHub Actions workflow is configured to sign the APK using secrets. You will need to provide the following secrets in your repository's settings:

*   `SIGNING_KEY_BASE64`: The base64-encoded signing key.
*   `ALIAS`: The alias for the key.
*   `KEY_STORE_PASSWORD`: The password for the keystore.
*   `KEY_PASSWORD`: The password for the key itself.

## 📄 License

This project is open-source and available under the [MIT License](LICENSE).
