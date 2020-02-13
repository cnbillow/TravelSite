$(function(){
    // 创建地图
    let map = new  BMap.Map("map");
    let point = new BMap.Point(103.0076674998, 29.9848521129); 
    map.centerAndZoom(point, 15); 
    map.enableScrollWheelZoom(true);
    map.addControl(new BMap.NavigationControl());    
    map.addControl(new BMap.ScaleControl());    
    map.addControl(new BMap.OverviewMapControl());    
    map.addControl(new BMap.MapTypeControl());
    map.setCurrentCity("四川农业大学");
    // 创建标注    
    var marker = new BMap.Marker(point);        
    map.addOverlay(marker);    
});