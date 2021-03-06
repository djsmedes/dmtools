// See http://brunch.io for documentation.
exports.paths = {
    public: '../dist/',
    watched: ['js', 'css', 'scss']
};

exports.files = {
    javascripts: {
        joinTo: {
            'js/app.js': /^js/,
            'js/vendor.js': /^node_modules/
        }
    },
    stylesheets: { joinTo: 'css/app.css' }
};

exports.plugins = {
    babel: {
        presets: ['env']
    },
    sass: {
        precision: 8
    },
    postcss: {
        processors: [
            require('autoprefixer')(['last 8 versions']),
            require('csswring')()
        ]
    }
};

exports.modules = {
    autoRequire: {
        'js/app.js': ['js/initialize']
    }
};

exports.npm = {
    globals: {
        $: 'jquery',
        jQuery: 'jquery',
        bootstrap: 'bootstrap'
    }
};