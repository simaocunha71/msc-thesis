```php
<?php
class WebAssets
{
    public $basePath;
    public $baseUrl;
    public $cssFiles = [];
    public $jsFiles = [];
    public $dependencies = [];

    public function registerAssets()
    {
        // Register CSS files
        foreach ($this->cssFiles as $cssFile) {
            Yii::$app->assetManager->registerCssFile($this->baseUrl . $cssFile);
        }

        // Register JavaScript files
        foreach ($this->jsFiles as $jsFile) {
            Yii::$app->assetManager->registerJsFile($this->baseUrl . $jsFile);
        }

        // Register dependencies
        foreach ($this->dependencies as $dependency) {
            Yii::$app->assetManager->registerAssetBundle($dependency);
        }
    }
}
?>
```