    class AssetSet extends CApplicationComponent
    {
        public $basePath;
        public $baseUrl;
        public $css;
        public $js;
        public $deps;

        public function init()
        {
            // Set the base path and URL
            $this->basePath = Yii::app()->basePath . '/assets';
            $this->baseUrl = Yii::app()->baseUrl . '/assets';

            // Define the CSS files
            $this->css = array(
                'css/bootstrap.css',
                'css/custom.css',
            );

            // Define the JavaScript files
            $this->js = array(
                'js/bootstrap.js',
                'js/custom.js',
            );

            // Define the dependencies on other assets
            $this->deps = array(
                'bootstrap' => array(
                    'css' => array('bootstrap.css'),
                    'js' => array('bootstrap.js'),
                ),
                'custom' => array(
                    'css' => array('custom.css'),
                    'js' => array('custom.js'),
                ),
            );
        }
    }

