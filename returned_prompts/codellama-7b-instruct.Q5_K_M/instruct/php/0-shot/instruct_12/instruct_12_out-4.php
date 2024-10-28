
    class AssetManager
    {
        public $basePath = '@webroot';
        public $baseUrl = '@web';
        public $css = [
            'css/site.css',
        ];
        public $js = [
        ];
        public $depends = [
            'yii\web\YiiAsset',
            'yii\bootstrap\BootstrapAsset',
            'yii\bootstrap\BootstrapPluginAsset',
        ];
    }

