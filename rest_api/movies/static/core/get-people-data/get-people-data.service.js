'use strict';

angular.
  module('core.getPeopleData').
  factory('PeopleService', ['$resource',
    function($resource) {
      return $resource('/person', {}, {
        query: {
          method: 'GET',
          params: {},
          isArray: true
        }
      });
    }
  ]);
