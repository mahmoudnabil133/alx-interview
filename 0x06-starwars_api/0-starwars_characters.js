#!/usr/bin/env node
// request module for making http requests
const request = require('request');

request(`https://swapi-api.alx-tools.com/api/films/${process.argv[2]}`, async (error, response, body)=>{
    if (error) {
        console.log(error);
    } else if (response.statusCode === 200) {
        const film = JSON.parse(body)
        const stars = film.characters
        for (starUrl of stars) {
            await new Promise((resolve, reject)=>{
                request(starUrl, (error, response, body)=>{
                    if (error) {
                        reject(error)
                    } else if (response.statusCode === 200) {
                        const charcterData = JSON.parse(body)
                        const charName = charcterData.name
                        console.log(charName)
                        resolve()
                    }
                })
            })
        }
    } else {
        console.log('failed to feach data, statusCode:', response.statusCode)
    }
})
