
var myApp = angular.module('myApp', ['ui.router']);

myApp.config(function($stateProvider, $urlRouterProvider) {

    $urlRouterProvider.otherwise("/");

    $stateProvider
        .state("state1", {
            url: "/",
            templateUrl: "static/partials/home.html"
        });

    $stateProvider
        .state("state2", {
            url: "/vis",
            templateUrl: "static/partials/home2.html"
        });

});
