import { Component, ViewEncapsulation } from '@angular/core';

@Component({
  selector: 'transactions-card',
  templateUrl: './Rating-card.component.html',
  styleUrls: ['./Rating-card.component.scss'],
  encapsulation: ViewEncapsulation.None,
  host: {
    '[class.Rating-card]': 'true'
  }
})

export class RatingCardComponent {


}