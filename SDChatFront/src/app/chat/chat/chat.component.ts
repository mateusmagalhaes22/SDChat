import { Component, OnInit } from '@angular/core';


export interface Message {
  user: string;
  content: string;
  msgDate: string;
}

const data: Message[] = [ {"user": "mateus", "content":"olá", "msgDate":"dane-se"} ];

@Component({
  selector: 'app-chat',
  templateUrl: './chat.component.html',
  styleUrls: ['./chat.component.scss']
})
export class ChatComponent implements OnInit{
  ngOnInit(): void {
    console.log(this.dataSource);
    console.log(data);
  }
  dataSource = data;

}
