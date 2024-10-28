    class AssetManager extends CAssetManager
    {
        public $basePath = null;
        public $baseUrl = null;
        public $js = array();
        public $css = array();
        public $depends = array(
            'bootstrap.widgets.BootstrapAsset',
            'bootstrap.widgets.BootstrapPluginAsset'
        );
    }

