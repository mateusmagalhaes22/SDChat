import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { MensagensModule } from './mensagens/mensagens.module';

const routes: Routes = [
  { path: "", pathMatch: "full", redirectTo: "messages" },
  { path: "messages", loadChildren: () => import('./mensagens/mensagens.module').then(m => m.MensagensModule) }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
