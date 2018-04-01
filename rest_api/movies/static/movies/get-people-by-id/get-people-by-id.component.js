'use strict';

// Register `getPeopleById'` component, along with its associated controller and template
angular.
  module('getPeopleByIdData').
  component('getPeopleById', {
    templateUrl: 'static/movies/get-people-by-id/get-people-by-id.template.html',
    controller: ['$routeParams', 'PeopleByIdService',
      function myController($routeParams, PeopleByIdService) {
        var self = this;
        self.person = PeopleByIdService.get({id: $routeParams.id})
    }]
  });
