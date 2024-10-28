<?php

use yii\web\AssetBundle;
use yii\bootstrap\BootstrapAsset;
use yii\bootstrap\BootstrapPluginAsset;

class WebAppAssets extends AssetBundle
{
    public $basePath = '@webroot';
    public $baseUrl = '@web';
    public $css = [];
    public $js = [];
    public $depends = [];

    public function __construct()
    {
        $this->css = [
            'css/site.css',
        ];

        $this->js = [
            'js/site.js',
        ];

        $this->depends = [
            BootstrapAsset::class,
            BootstrapPluginAsset::class,
        ];

        parent::__construct();
    }
}

