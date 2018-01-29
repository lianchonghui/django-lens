$(function(){
    // 页数
    var page = 0;
    // 每页展示5个
    var size = 8;
    var thumbnail=$(".thumbnail");
    thumbnail.click(function(){alert("hello");});

    // dropload
    $('.session').dropload({
        //scrollArea : window,
        loadDownFn : function(me){
            page++;
            // 拼接HTML
            var result = '';
            $.ajax({
                async: false,
                type: 'GET',
                url: 'lens/?page='+page+'&size='+size,
                dataType: 'json',
                success: function(data){
                    alert(data[0].full);
                    var arrLen = data.length;
                    if(arrLen > 0){
                        for(var i=0; i<arrLen; i++){
                            result += '<article>'
							                +'<a class="thumbnail" href="'+data[i].full+'" data-position="left center"><img src="'+data[i].thumb+'" alt="" /></a>'
							                +'<h2>'+data[i].name+'</h2>'
							                +'<p>'+data[i].description+'</p>'
						                    +'</article>';
                        }
                    // 如果没有数据
                    }else{
                        // 锁定
                        me.lock();
                        // 无数据
                        me.noData();
                    }
                    // 为了测试，延迟1秒加载
                    setTimeout(function(){
                        // 插入数据到页面，放到最后面
                        //alert(result);
                        $('.thumbscroll').append(result);
                        $('.thubmnail').trigger("thumbnail");
                        // 每次数据插入，必须重置
                        me.resetload();
                    },1000);
                },
                error: function(xhr, type){
                    alert('Ajax error!');
                    // 即使加载出错，也得重置
                    me.resetload();
                }
            });
        }
    });
});