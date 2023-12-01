import { FormControl, FormGroup } from '@angular/forms';
import { MensagensService } from '../mensagens.service';
import { mensagem } from './../mensagem';
import { Component, ElementRef, OnInit, ViewChild } from '@angular/core';

@Component({
  selector: 'app-mensagens',
  templateUrl: './mensagens.component.html',
  styleUrls: ['./mensagens.component.scss']
})
export class MensagensComponent implements OnInit {

  newMessageForm!: FormGroup;

  constructor(private service: MensagensService){}

  mensagens: mensagem[] = [];
  dataSource = this.mensagens;
  displayedColumns: string[] = ['conteudo'];

  ngOnInit(): void {
    this.service.list().subscribe(data => {
      this.mensagens = data
      this.dataSource = this.mensagens
    })

    this.newMessageForm = new FormGroup({
      usuario: new FormControl(''),
      conteudo: new FormControl('')
    })
  }

  enviar() {
    var msg = this.newMessageForm.value;
    console.log(msg);

    this.service.post(msg);

    window.location.reload();
  }
}
