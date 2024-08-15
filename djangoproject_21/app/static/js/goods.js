//新增货物模态框函数
function Goodsadd(){
    /*建立模态框对象*/
    modalBox = {};
    /*获取模var态框*/
    modalBox.modal = document.getElementById("myModalGoods");
    /*获得新增按钮*/
    modalBox.triggerBtn = document.getElementById("addGoods");
    /*获得添加货物界面的关闭按钮*/
    modalBox.closeBtn = document.getElementById("closeBtnGoods");
    /*模态框显示*/
    modalBox.show = function() {
        console.log(this.modal);
        this.modal.style.display = "block";
    }
    /*模态框关闭*/
    modalBox.close = function() {
        this.modal.style.display = "none";
    }
    /*当用户点击模态框内容之外的区域，模态框也会关闭*/
    modalBox.outsideClick = function() {
        var modal = this.modal;
        window.onclick = function(event) {
            if(event.target == modal) {
                modal.style.display = "none";
            }
        }
    }
    /*模态框初始化*/
    modalBox.init = function() {
        var that = this;
        this.triggerBtn.onclick = function() {
            that.show();
        }
        this.closeBtn.onclick = function() {
            that.close();
        }
        this.outsideClick();

    }
    modalBox.init();
}

// 编写函数完成指定数据删除请求的发送
function deleteGoodsById(goodsId){
    console.log("删除货物编号:" + goodsId);
    // 使用js提示对话框
    if(confirm("确定删除数据吗?")){
        // 删除数据，发送删除的url请求
        url = "/app/deleteGoods/delete/" + goodsId;
        console.log(url);
        // 发送GET请求
        window.location = url;
    }
    else{
        url=window.location.href;
        window.location.assign(url);
    }
}

//查看
function GoodsById(storeId){
    url = "/app/gotoGoods/goto/" + storeId;
    window.location = url;
}

//查找货物模态框函数
function Goodsinquiry(){
    /*建立模态框对象*/
    modalBox = {};
    /*获取模var态框*/
    modalBox.modal = document.getElementById("inquiryModalGoods");
    /*获得货物查询按钮*/
    modalBox.triggerBtn = document.getElementById("findGoods");
    /*获得货物界面的关闭按钮*/
    modalBox.closeBtn = document.getElementById("inquirycloseBtnGoods");
    
    /*模态框显示*/
    modalBox.show = function() {
        console.log(this.modal);
        this.modal.style.display = "block";
    }
    /*模态框关闭*/
    modalBox.close = function() {
        this.modal.style.display = "none";
    }
    /*当用户点击模态框内容之外的区域，模态框也会关闭*/
    modalBox.outsideClick = function() {
        var modal = this.modal;
        window.onclick = function(event) {
            if(event.target == modal) {
                modal.style.display = "none";
            }
        }
    }
    /*模态框初始化*/
    modalBox.init = function() {
        var that = this;
        this.triggerBtn.onclick = function() {
            that.show();
        }
        this.closeBtn.onclick = function() {
            that.close();
        }
        this.outsideClick();
    }
    modalBox.init();
}

//更新货物模态框函数
function GoodsupdateAjax(goodsId){
    $.ajax({
        async: true,
        url: "/app/transGoods/trans/"+goodsId,
        type: "post",
        headers: {"X-CSRFToken":$.cookie("csrftoken")},

        success: function(goods){
            /*建立模态框对象*/
            modalBox = {};
            /*获取模var态框*/
            modalBox.modal = document.getElementById("updateModalGoods");
            /*获得货物更新按钮*/
            modalBox.triggerBtn = document.getElementById("tablelistGoods");
            /*获得货物界面的关闭按钮*/
            modalBox.closeBtn = document.getElementById("updatecloseBtnGoods");
            /* */
            modalBox.inputId1 = document.getElementById("updategoodsId1");
            modalBox.inputId2 = document.getElementById("updategoodsId2");
            modalBox.inputName = document.getElementById("updategoodsName");
            modalBox.inputType = document.getElementById("updategoodsType");
            modalBox.inputStore1 = document.getElementById("updategoodsStore1");
            modalBox.inputStore2 = document.getElementById("updategoodsStore2");
            modalBox.inputAmount = document.getElementById("updategoodsAmount");
            modalBox.inputShelves = document.getElementById("updategoodsShelves");

            // 需要知道后端字典的键
            modalBox.inputId1.value=goods.showgoodsId;
            modalBox.inputId2.value=goods.showgoodsId;
            modalBox.inputName.value=goods.showgoodsName;
            modalBox.inputType.value=goods.showgoodsType;
            modalBox.inputStore1.value=goods.showgoodsStore;
            modalBox.inputStore2.value=goods.showgoodsStore;
            modalBox.inputAmount.value=goods.showgoodsAmount;
            modalBox.inputShelves.value=goods.showgoodsShelves;

            /*模态框显示*/
            modalBox.show = function() {
                console.log(this.modal);
                this.modal.style.display = "block";
            }
            /*模态框关闭*/
            modalBox.close = function() {
                this.modal.style.display = "none";
            }
            /*当用户点击模态框内容之外的区域，模态框也会关闭*/
            modalBox.outsideClick = function() {
                var modal = this.modal;
                window.onclick = function(event) {
                    if(event.target == modal) {
                        modal.style.display = "none";
                    }
                }
            }
            /*模态框初始化*/
            modalBox.init = function() {
                var that = this;
                
                this.triggerBtn.onclick = function() {
                    
                    that.show();
                    
                }
                this.closeBtn.onclick = function() {
                    that.close();
                }
                this.outsideClick();
            }
            modalBox.init();
        }
        
    });
        
}

//导入函数
function GoodsbatchImport(){
    $("#batchImportGoods").change(function(){
        // 使用Ajax实现文件上传操作
        // 创建一个FormData对象，用于存放上传图片的数据
        var form_data = new FormData();
        // 读取上传图片的数据
        var file_info = $("#batchImportGoods")[0].files[0];
        // 将读取到的二进制数据添加到formData对象中
        form_data.append("file", file_info);
        // 使用Ajax发送异步请求并携带请求数据
        $.ajax({
            async: true,
            url: "/app/ajax/picupload/",
            type: "post",
            headers: {"X-CSRFToken":$.cookie("csrftoken")},
            data: form_data,
            processData: false,
            contentType: false,
            success: function(data){
                alert(data);
                // 获取图片元素修改其src属性值
                // $("#photo").attr("src", data);
                // // 分割用户头像的url地址
                // var photoname = data.split("/")[3];
                // // 将用户头像图片名称添加到隐藏域组件中
                // $("#photoname").attr("value", photoname);
            }
        });
    });
}