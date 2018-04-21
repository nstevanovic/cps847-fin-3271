import { Injectable } from '@angular/core';
import { Http } from '@angular/http';
import 'rxjs/add/operator/map';

@Injectable()
export class DataService {

	constructor(public http:Http) { 
		console.log('Data service consructed')
	}
	
	getWeather(){
		return this.http.get('https://api.wunderground.com/api/<api-key>/conditions/q/Ontario/Kingston.json').map(res => res.json())
	}

}
