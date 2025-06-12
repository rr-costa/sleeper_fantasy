import { FormsModule } from '@angular/forms';

@NgModule({
  declarations: [
    AppComponent
  ],
  imports: [
    BrowserModule,
    FormsModule  // <--- Importar aqui
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
