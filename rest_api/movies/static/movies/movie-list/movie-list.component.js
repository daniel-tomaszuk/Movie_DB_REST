'use strict';

// Register `phoneList` component, along with its associated controller and template
angular.
  module('movieList').
  component('movieList', {
    templateUrl: 'static/movies/movie-list/movie-list.template.html',
    controller: ['MovieService',
      function myController(MovieService) {
        this.movies = MovieService.query();
        this.orderProp = 'year';
    }]
  });
