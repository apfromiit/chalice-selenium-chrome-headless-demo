## Chalice Selenium Chrome Headless Demo

This is a demo of below project using Chalice.

https://github.com/apfromiit/lambda-selenium-chrome-headless-demo

## Notes

Works with `python 3.7` only

Need to find chrome drivers and selenium version that works with latest python version supported by AWS Lambda.

## Deployment

> sh lambda-layer.sh

Update `layers` in `config.json`

> chalice deploy

## Reference

https://robertorocha.info/setting-up-a-selenium-web-scraper-on-aws-lambda-with-python