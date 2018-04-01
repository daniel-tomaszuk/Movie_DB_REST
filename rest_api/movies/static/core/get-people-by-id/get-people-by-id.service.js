'use strict';

angular.
  module('core.getPeopleByIdData').
  factory('PeopleByIdService', ['$resource',
    function($resource) {
      return $resource('/person/:id', {}, {
        query: {
          method: 'GET',
          params: {},
          isArray: false
        }
      });
    }
  ]);
