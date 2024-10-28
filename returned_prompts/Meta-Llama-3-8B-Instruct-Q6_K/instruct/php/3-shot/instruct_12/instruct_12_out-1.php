    class AssetBundle extends \yii\web\AssetBundle
    {
        public $basePath;
        public $baseUrl;
        public $css = [];
        public $js = [];
        public $depends = [];

        public function __construct($id, $basePath, $baseUrl, $css = [], $js = [], $depends = [])
        {
            parent::__construct($id);
            $this->basePath = $basePath;
            $this->baseUrl = $baseUrl;
            $this->css = $css;
            $this->js = $js;
            $this->depends = $depends;
        }
    }

    class BootstrapAsset extends AssetBundle
    {
        public $sourcePath = '@bower/bootstrap/dist';

        public function init()
        {
            $this->css[] = 'css/bootstrap.css';
            $this->js[] = 'js/bootstrap.js';
            parent::init();
        }
    }

    class BootstrapPluginAsset extends AssetBundle
    {
        public $sourcePath = '@bower/bootstrap/dist';

        public function init()
        {
            $this->css[] = 'css/bootstrap-theme.css';
            $this->js[] = 'js/bootstrap-theme.js';
            parent::init();
        }
    }