    ```php
    class Assets {
        public $basePath;
        public $baseUrl;
        public $cssFiles = array();
        public $jsFiles = array();
        public $dependencies = array();

        public function __construct($basePath, $baseUrl) {
            $this->basePath = $basePath;
            $this->baseUrl = $baseUrl;
        }

        public function addCssFile($file) {
            $this->cssFiles[] = $file;
        }

        public function addJsFile($file) {
            $this->jsFiles[] = $file;
        }

        public function addDependency(Assets $asset) {
            $this->dependencies[] = $asset;
        }

        public function getBootstrapAsset() {
            return Yii::app()->assetManager->publish($this->basePath . '/css/bootstrap.css');
        }

        public function getBootstrapPluginAsset() {
            return Yii::app()->assetManager->publish($this->basePath . '/js/bootstrap.plugin.js');
        }
    }
    ```

















```php
<?php

class Assets {
    public $basePath;
    public $baseUrl;
    public $cssFiles = array();
    public $jsFiles = array();
    public $dependencies = array();

    public function __construct($basePath, $baseUrl) {
        $this->basePath = $basePath;
        $this->baseUrl = $baseUrl;
    }

    public function addCssFile($file) {
        $this->cssFiles[] = $file;
    }

    public function addJsFile($file) {
        $this->jsFiles[] = $file;
    }

    public function addDependency(Assets $asset) {
        $this->dependencies[] = $asset;
    }

    public function getBootstrapAsset() {
        return Yii::app()->assetManager->publish($this->basePath . '/css/bootstrap.css');
    }

    public function getBootstrapPluginAsset() {
        return Yii::app()->assetManager->publish($this->basePath . '/js/bootstrap.plugin.js');
    }
}
```







```php
<?php

class Assets {
    public $basePath;
    public $baseUrl;
    public $cssFiles = array();
    public $jsFiles = array();
    public $dependencies = array();

    public function __construct($basePath, $baseUrl) {
        $this->basePath = $basePath;
        $this->baseUrl = $baseUrl;
    }

    public function addCssFile($file) {
        $this->cssFiles[] = $file