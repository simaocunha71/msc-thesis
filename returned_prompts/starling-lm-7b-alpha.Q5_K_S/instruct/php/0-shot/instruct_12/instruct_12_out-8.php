    class Assets extends \yii\web\AssetBundle
    {
        public $sourcePath = '@app/assets';
        public $basePath = '@webroot';
        public $baseUrl = '@web';

        public $css = [
            'css/bootstrap.min.css',
        ];

        public $js = [
            'js/bootstrap.min.js',
        ];

        public $depends = [
            '\yii\bootstrap\BootstrapAsset',
            '\yii\bootstrap\BootstrapPluginAsset',
        ];
    }

