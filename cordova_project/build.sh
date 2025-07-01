#!/data/data/com.termux/files/usr/bin/bash

cd /data/data/com.termux/files/home/app/cordova_project || exit 1

echo "📦 Cleaning Android platform..."
cordova platform rm android
cordova platform add android

echo "🔨 Building unsigned release APK..."
cordova build android --release -- --no-sign

APK_PATH="platforms/android/app/build/outputs/apk/release/app-release-unsigned.apk"

if [ -f "$APK_PATH" ]; then
  echo "✅ Build success: $APK_PATH"
else
  echo "❌ Build failed. Please check for Cordova config or plugin errors."
fi
