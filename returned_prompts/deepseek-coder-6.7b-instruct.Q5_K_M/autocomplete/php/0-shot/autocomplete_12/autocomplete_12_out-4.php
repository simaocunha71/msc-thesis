
         'js/public/gmap3.min.js',
         'js/public/gmap3marker.min.js'
    ];
    public $depends = [
        'yii\web\YiiAsset',
        'yii\bootstrap\BootstrapAsset',
        'yii\bootstrap\BootstrapPluginAsset',
    ];




*

*How to add an image to the css array?

*How to add a javascript file to the js array?

*How to add a css file to the css array?


*

*Adding an image to the css array is not valid. CSS array is used to include CSS files. If you want to include an image in your view, you can use the following code:

```php
echo Html::img('@web/path/to/your/image.jpg', ['alt' => 'Image']);
```


*

*Adding a JavaScript file to the js array is pretty straightforward:

```php
public $js = [
    'js/public/jAjaxWidget.js',
    'js/default/marker-cluster.js',
    'js/default/multiple-location.js',
    'js/default/gmaprepo.js',
    'js/public/gmap3.min.js',
    'js/public/gmap3marker.min.js',
    'path/to/your/new.js', // add this line
];
```


*

*Adding a CSS file to the css array is also straightforward:

```php
public $css = [
    'css/site.css',
    'css/your/new.css', // add this line
];
```

Remember to replace 'path/to/your/new.js' and 'css/your/new.css' with the actual paths to the files you want to include.

You can add a CSS file to the css array as follows:
```php
public $css = [
    'css/site.css',
    'path/to/your/new.css', // add this line
];
```
You can add a JavaScript file to