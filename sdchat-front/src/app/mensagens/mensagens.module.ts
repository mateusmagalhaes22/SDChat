import { CommonModule } from '@angular/common';
import { NgModule } from '@angular/core';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { MatButtonModule } from '@angular/material/button';
import { MatFormFieldModule } from '@angular/material/form-field';
import { MatInputModule } from '@angular/material/input';
import { MatSelectModule } from '@angular/material/select';
import { MatTableModule } from '@angular/material/table';

import { MensagensRoutingModule } from './mensagens-routing.module';
import { MensagensComponent } from './mensagens/mensagens.component';


@NgModule({
  declarations: [
    MensagensComponent
  ],
  imports: [
    CommonModule,
    MensagensRoutingModule,
    MatTableModule,
    MatFormFieldModule,
    MatInputModule,
    MatSelectModule,
    MatButtonModule,
    FormsModule,
    ReactiveFormsModule
  ]
})
export class MensagensModule {

}
