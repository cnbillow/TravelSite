$(function() {
    //处理描述
    $(function() {
        // 处理描述/评论切换
        $(".tab-menu-list li").click(function() {
            // 获取选中菜单下标
            let index = $(this).index();
    
            $(".tab-ct-list li")
            .eq(index)
            .addClass("show")
            .siblings()
            .removeClass("show");
    
            $(this)
            .addClass("sel")
            .siblings()
            .removeClass("sel");
        });
    });
    

    // 获取数据
    const data = Model.GET("setMeal");
    loadingMoreList(); 
    function loadingMoreList() {
        let list = null;
        let type = 1;
        list = data.filter(item => item.type == type);
        console.log(list);
        $(".information-list").html(
            (function() {
                let lis = list.map(item => {
                    return `<li> 
                                <div class="img">
                                    <img src="../images/${item.imgUrl}">
                                </div>
                                <p class="title">${item.title}</p>
                            </li>`;
                        });
                        return lis.join("");
                    }
            )
            ());

        // let.map((item, index)=> {if(index<4){retrn}})
        // 
        // 
        // 
        // 
        // 
        // 
        // 
        // 
        // 
        // 
        //          
        //
    }
});