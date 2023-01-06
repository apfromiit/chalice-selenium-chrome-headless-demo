mkdir bin
cd bin
curl -SL https://chromedriver.storage.googleapis.com/2.37/chromedriver_linux64.zip > chromedriver.zip
curl -SL https://github.com/adieuadieu/serverless-chrome/releases/download/v1.0.0-37/stable-headless-chromium-amazonlinux-2017-03.zip > headless-chromium.zip
unzip chromedriver.zip
unzip headless-chromium.zip
rm chromedriver.zip
rm headless-chromium.zip
cd ..
zip -yr bin.zip bin
mv bin.zip chromedriver.zip
rm -rf bin
aws lambda publish-layer-version --layer-name chromedriver --zip-file fileb://chromedriver.zip --description "Headless Chrome Driver"  --compatible-runtimes python3.7
rm chromedriver.zip