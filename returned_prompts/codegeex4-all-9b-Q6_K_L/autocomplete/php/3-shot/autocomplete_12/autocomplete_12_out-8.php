 // gmap repo
        'js/default/infobox.js', // infobox
        'js/default/route.js', // route
        'js/default/cluster.js', // cluster
        'js/default/map.js', // map
    ];
    public $depends = [
        'yii\web\YiiAsset',
        'yii\web\JqueryAsset',
        'yii\bootstrap\BootstrapAsset',
        'app\assets\GmapAsset',
    ];
    public $options = [
        'packages' => [
            'gmap3' => [
                'type' => 'js',
                'location' => '//cdn.jsdelivr.net/gmap3/5.1.1/gmap3.min.js',
            ],
            'infobox' => [
                'type' => 'js',
                'location' => '//cdn.jsdelivr.net/g/infobox-polyfill/1.1.14/infobox.min.js',
            ],
            'markerwithlabel' => [
                'type' => 'js',
                'location' => '//cdn.jsdelivr.net/g/markerwithlabel/2.1.2/markerwithlabel.min.js',
            ],
            'cluster' => [
                'type' => 'js',
                'location' => '//cdn.jsdelivr.net/g/marker-clusterer/2.1.2/markerclusterer.min.js',
            ],
            'route' => [
                'type' => 'js',
                'location' => '//maps.googleapis.com/maps/api/js?v=3.exp&libraries=places',
            ],
        ],
    ];

    public $options = [
        'packages' => [
            'gmap3' => [
                'type' => 'js',
                'location' => '//cdn.jsdelivr.net/gmap3/5.1.1/gmap3.min.js',
            ],
            'infobox' => [
                'type' => 'js',
                'location' => '//cdn.jsdelivr.net/g/infobox-polyfill/1.1.14/infobox.min.js',
            ],
            'markerwithlabel' => [
                'type' => 'js',
                'location' => '//cdn.jsdelivr.net/g/markerwithlabel/2.1.2/markerwithlabel.min.js',
            ],
            'cluster' => [
                'type' => 'js',
                'location' => '//cdn.jsdelivr.net/g/marker-clusterer/2.1.2/markerclusterer.min.js',
           