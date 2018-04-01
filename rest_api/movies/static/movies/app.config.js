'use strict';

angular.
  module('myApp').
  config(['$locationProvider' ,'$routeProvider',
    function config($locationProvider, $routeProvider) {
      $locationProvider.hashPrefix('!');

      $routeProvider.
        when('/', {
          template: '<movie-list></movie-list><people-list></people-list>'
        }).
        when('/person/:id', {
          template: '<get-people-by-id></get-people-by-id>'
        }).
        otherwise('/');
    }
  ]);
