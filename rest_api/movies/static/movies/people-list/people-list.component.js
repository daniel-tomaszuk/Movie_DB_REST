'use strict';

// Register `phoneList` component, along with its associated controller and template
angular.
  module('peopleList').
  component('peopleList', {
    templateUrl: 'static/movies/people-list/people-list.template.html',
    controller: ['PeopleService',
      function myController(PeopleService) {
        this.people = PeopleService.query();
        this.orderProp = 'name';
    }]
  });
