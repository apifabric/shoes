import { MenuRootItem } from 'ontimize-web-ngx';

import { CustomerCardComponent } from './Customer-card/Customer-card.component';

import { EmployeeCardComponent } from './Employee-card/Employee-card.component';

import { InventoryCardComponent } from './Inventory-card/Inventory-card.component';

import { OrderCardComponent } from './Order-card/Order-card.component';

import { OrderItemCardComponent } from './OrderItem-card/OrderItem-card.component';

import { ProductCardComponent } from './Product-card/Product-card.component';

import { ProductPromotionCardComponent } from './ProductPromotion-card/ProductPromotion-card.component';

import { PromotionCardComponent } from './Promotion-card/Promotion-card.component';

import { RatingCardComponent } from './Rating-card/Rating-card.component';

import { ShipmentCardComponent } from './Shipment-card/Shipment-card.component';

import { StoreCardComponent } from './Store-card/Store-card.component';

import { SupplierCardComponent } from './Supplier-card/Supplier-card.component';


export const MENU_CONFIG: MenuRootItem[] = [
    { id: 'home', name: 'HOME', icon: 'home', route: '/main/home' },
    
    {
    id: 'data', name: ' data', icon: 'remove_red_eye', opened: true,
    items: [
    
        { id: 'Customer', name: 'CUSTOMER', icon: 'view_list', route: '/main/Customer' }
    
        ,{ id: 'Employee', name: 'EMPLOYEE', icon: 'view_list', route: '/main/Employee' }
    
        ,{ id: 'Inventory', name: 'INVENTORY', icon: 'view_list', route: '/main/Inventory' }
    
        ,{ id: 'Order', name: 'ORDER', icon: 'view_list', route: '/main/Order' }
    
        ,{ id: 'OrderItem', name: 'ORDERITEM', icon: 'view_list', route: '/main/OrderItem' }
    
        ,{ id: 'Product', name: 'PRODUCT', icon: 'view_list', route: '/main/Product' }
    
        ,{ id: 'ProductPromotion', name: 'PRODUCTPROMOTION', icon: 'view_list', route: '/main/ProductPromotion' }
    
        ,{ id: 'Promotion', name: 'PROMOTION', icon: 'view_list', route: '/main/Promotion' }
    
        ,{ id: 'Rating', name: 'RATING', icon: 'view_list', route: '/main/Rating' }
    
        ,{ id: 'Shipment', name: 'SHIPMENT', icon: 'view_list', route: '/main/Shipment' }
    
        ,{ id: 'Store', name: 'STORE', icon: 'view_list', route: '/main/Store' }
    
        ,{ id: 'Supplier', name: 'SUPPLIER', icon: 'view_list', route: '/main/Supplier' }
    
    ] 
},
    
    { id: 'settings', name: 'Settings', icon: 'settings', route: '/main/settings'}
    ,{ id: 'about', name: 'About', icon: 'info', route: '/main/about'}
    ,{ id: 'logout', name: 'LOGOUT', route: '/login', icon: 'power_settings_new', confirm: 'yes' }
];

export const MENU_COMPONENTS = [

    CustomerCardComponent

    ,EmployeeCardComponent

    ,InventoryCardComponent

    ,OrderCardComponent

    ,OrderItemCardComponent

    ,ProductCardComponent

    ,ProductPromotionCardComponent

    ,PromotionCardComponent

    ,RatingCardComponent

    ,ShipmentCardComponent

    ,StoreCardComponent

    ,SupplierCardComponent

];