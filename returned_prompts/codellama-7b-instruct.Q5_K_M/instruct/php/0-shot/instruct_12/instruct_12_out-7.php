
    Example:

    class Assets {
        public static $basePath = '@webroot';
        public static $baseUrl = '@web';
        public static $css = [
            'css/site.css',
        ];
        public static $js = [
            'js/main.js',
        ];
        public static $depends = [
            'yii\bootstrap\BootstrapAsset',
            'yii\bootstrap\BootstrapPluginAsset',
        ];
    }

    *********************************************************************/

class Assets {
    public static $basePath = '@webroot';
    public static $baseUrl = '@web';
    public static $css = [
        'css/site.css',
    ];
    public static $js = [
        'js/main.js',
    ];
    public static $depends = [
        'yii\bootstrap\BootstrapAsset',
        'yii\bootstrap\BootstrapPluginAsset',
    ];
}
