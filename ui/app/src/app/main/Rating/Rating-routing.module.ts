import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { RatingHomeComponent } from './home/Rating-home.component';
import { RatingNewComponent } from './new/Rating-new.component';
import { RatingDetailComponent } from './detail/Rating-detail.component';

const routes: Routes = [
  {path: '', component: RatingHomeComponent},
  { path: 'new', component: RatingNewComponent },
  { path: ':id', component: RatingDetailComponent,
    data: {
      oPermission: {
        permissionId: 'Rating-detail-permissions'
      }
    }
  }
];

export const RATING_MODULE_DECLARATIONS = [
    RatingHomeComponent,
    RatingNewComponent,
    RatingDetailComponent 
];


@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class RatingRoutingModule { }