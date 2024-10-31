import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { ProductHomeComponent } from './home/Product-home.component';
import { ProductNewComponent } from './new/Product-new.component';
import { ProductDetailComponent } from './detail/Product-detail.component';

const routes: Routes = [
  {path: '', component: ProductHomeComponent},
  { path: 'new', component: ProductNewComponent },
  { path: ':id', component: ProductDetailComponent,
    data: {
      oPermission: {
        permissionId: 'Product-detail-permissions'
      }
    }
  },{
    path: ':product_id/Inventory', loadChildren: () => import('../Inventory/Inventory.module').then(m => m.InventoryModule),
    data: {
        oPermission: {
            permissionId: 'Inventory-detail-permissions'
        }
    }
},{
    path: ':product_id/OrderItem', loadChildren: () => import('../OrderItem/OrderItem.module').then(m => m.OrderItemModule),
    data: {
        oPermission: {
            permissionId: 'OrderItem-detail-permissions'
        }
    }
},{
    path: ':product_id/ProductPromotion', loadChildren: () => import('../ProductPromotion/ProductPromotion.module').then(m => m.ProductPromotionModule),
    data: {
        oPermission: {
            permissionId: 'ProductPromotion-detail-permissions'
        }
    }
},{
    path: ':product_id/Rating', loadChildren: () => import('../Rating/Rating.module').then(m => m.RatingModule),
    data: {
        oPermission: {
            permissionId: 'Rating-detail-permissions'
        }
    }
},{
    path: ':product_id/Shipment', loadChildren: () => import('../Shipment/Shipment.module').then(m => m.ShipmentModule),
    data: {
        oPermission: {
            permissionId: 'Shipment-detail-permissions'
        }
    }
}
];

export const PRODUCT_MODULE_DECLARATIONS = [
    ProductHomeComponent,
    ProductNewComponent,
    ProductDetailComponent 
];


@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class ProductRoutingModule { }