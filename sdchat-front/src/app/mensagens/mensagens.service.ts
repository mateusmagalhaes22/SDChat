import { HttpClient } from '@angular/common/http'
import { Injectable } from '@angular/core';
import { mensagem } from './mensagem';

@Injectable({
  providedIn: 'root'
})
export class MensagensService {

  private readonly API = "http://localhost:4200/api/messages"

  constructor(private http:HttpClient) { }

  list() {
    return this.http.get<mensagem[]>(this.API);
  }

  post(mensagem: mensagem) {
    console.log(mensagem);
    this.http.post(this.API, mensagem).subscribe(r=>{});
  }
}
