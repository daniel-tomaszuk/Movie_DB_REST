'use strict';

angular.
  module('core.getMoviesByIdData').
  factory('MoviesByIdService', ['$resource',
    function($resource) {
      return $resource('/movie/:id', {}, {
        query: {
          method: 'GET',
          params: {},
          isArray: false
        }
      });
    }
  ]);
