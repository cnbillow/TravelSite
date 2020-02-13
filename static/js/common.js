$(function(){
    // 向后台请求数据
    $.ajax({
        url: "http://www.wwtliu.com/sxtstu/blueberrypai/getIndexBanner.php",
        success: (res) => {
            console.log(res);
        }
    });
    // 回到顶部
    $("aside .list > li").last().click(function(){
        // 触发回到顶部效果
        $("html, body").animate({
            scrollTop: 0
        }, 500);
    });
});