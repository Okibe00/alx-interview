#!/usr/bin/node
/**
 * prints characters from a star wars movie
 **/

const request = require('request');
const { argv } = require('node:process');

function getmovie (url) {
  const promise = new Promise(function (resolve, reject) {
    request(url, (error, response, body) => {
      if (response.statusCode === 200) {
        resolve(response.body);
      } else {
        reject(error);
      }
    });
  });
  return promise;
}

const url = `https://swapi-api.alx-tools.com/api/films/${argv[2]}/`;

function getJSON (url) {
  return getmovie(url).then(JSON.parse);
}

function getCharacters (url) {
  getJSON(url).then(movie => {
    return Promise.all(
      movie.characters.map(getJSON)
    );
  }).then(person => person.forEach(x => console.log(x.name)));
}
getCharacters(url);
