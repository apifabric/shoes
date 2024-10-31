import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { StoreHomeComponent } from './home/Store-home.component';
import { StoreNewComponent } from './new/Store-new.component';
import { StoreDetailComponent } from './detail/Store-detail.component';

const routes: Routes = [
  {path: '', component: StoreHomeComponent},
  { path: 'new', component: StoreNewComponent },
  { path: ':id', component: StoreDetailComponent,
    data: {
      oPermission: {
        permissionId: 'Store-detail-permissions'
      }
    }
  },{
    path: ':store_id/Shipment', loadChildren: () => import('../Shipment/Shipment.module').then(m => m.ShipmentModule),
    data: {
        oPermission: {
            permissionId: 'Shipment-detail-permissions'
        }
    }
}
];

export const STORE_MODULE_DECLARATIONS = [
    StoreHomeComponent,
    StoreNewComponent,
    StoreDetailComponent 
];


@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class StoreRoutingModule { }