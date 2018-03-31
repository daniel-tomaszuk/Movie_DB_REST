'use strict';

angular.
  module('core.getMoviesData').
  factory('MovieService', ['$resource',
    function($resource) {
      return $resource('/movie', {}, {
        query: {
          method: 'GET',
          params: {},
          isArray: true
        }
      });
    }
  ]);
