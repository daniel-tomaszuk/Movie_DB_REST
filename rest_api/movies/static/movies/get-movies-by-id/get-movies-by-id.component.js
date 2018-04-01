'use strict';

// Register `getMoviesById'` component, along with its associated controller and template
angular.
  module('getMoviesByIdData').
  component('getMoviesById', {
    templateUrl: 'static/movies/get-movies-by-id/get-movies-by-id.template.html',
    controller: ['$routeParams', 'MoviesByIdService',
      function myController($routeParams, MoviesByIdService) {
        var self = this;
        self.movie = MoviesByIdService.get({id: $routeParams.id})
    }]
  });
