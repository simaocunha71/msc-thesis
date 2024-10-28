
    class WebAssets extends CAssetManager {
        public $basePath = 'assets';
        public $baseUrl  = 'assets';
        public $cssFiles = array('css/main.css');
        public $jsFiles  = array('js/main.js');
        public $depends  = array('bootstrap.BootstrapAsset', 'bootstrap.BootstrapPluginAsset');
    }

