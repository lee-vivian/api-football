import { Component, OnInit } from '@angular/core';
import { FootballService } from './services/football.service';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss']
})
export class AppComponent implements OnInit {
  title = 'angular-api-football';

  constructor(
    private footballService: FootballService,
  ){}

  ngOnInit() {
    this.footballService.getStatus().subscribe({
      next: (result) => {
        console.log(result);
      },
      error: (err) => {
        console.log(err);
      }
    })
  }

}
