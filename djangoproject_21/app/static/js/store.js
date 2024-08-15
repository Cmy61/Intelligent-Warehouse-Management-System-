//添加仓库模态框函数
function add(){
    /*建立模态框对象*/
    modalBox = {};
    /*获取模var态框*/
    modalBox.modal = document.getElementById("myModal");
    /*获得更新按钮*/
    modalBox.triggerBtn = document.getElementById("addStore");
    /*获得关闭按钮*/
    modalBox.closeBtn = document.getElementById("closeBtn");
    /*模态框显示*/
    modalBox.show = function() {
        console.log(this.modal);
        this.modal.style.display = "block";
    }
    /*模态框关闭*/
    modalBox.close = function() {
        this.modal.style.display = "none";
        this.modal.on('hidden.bs.modal', function (){
            document.getElementById("contentForm").reset();
        });
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
function deleteDeptById(storeId){
    console.log("删除仓库编号:" + storeId);
    // 使用js提示对话框
    if(confirm("确定删除数据吗?")){
        // 删除数据，发送删除的url请求
        url = "/app/deleteStore/delete/" + storeId;
        console.log(url);
        // 发送GET请求
        window.location = url;
    }
    else{
        url="/app/index/";
        window.location.assign(url);
    }
}

//查找仓库模态框函数
function inquiry(){
    /*建立模态框对象*/
    modalBox = {};
    /*获取模var态框*/
    modalBox.modal = document.getElementById("inquiryModal");
    /*获得查询按钮*/
    modalBox.triggerBtn = document.getElementById("findStore");
    /*获得关闭按钮*/
    modalBox.closeBtn = document.getElementById("inquirycloseBtn");
    
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

//更新仓库模态框函数
function updateAjax(storeId){
    $.ajax({
        async: true,
        url: "/app/transStore/trans/"+storeId,
        type: "post",
        headers: {"X-CSRFToken":$.cookie("csrftoken")},

        success: function(store){
            console.log(store);
            /*建立模态框对象*/
            modalBox = {};
            /*获取模var态框*/
            modalBox.modal = document.getElementById("updateModal");
            /*获得更新按钮*/
            modalBox.triggerBtn = document.getElementById("tablelist");
            /*获得关闭按钮*/
            modalBox.closeBtn = document.getElementById("updatecloseBtn");
            /* */
            modalBox.inputId1 = document.getElementById("updatestoreId1");
            modalBox.inputId2 = document.getElementById("updatestoreId2");
            modalBox.inputName = document.getElementById("updatestoreName");
            modalBox.inputType = document.getElementById("updatestoreType");
            modalBox.inputLoca = document.getElementById("updatestoreLoca");
            modalBox.inputCap = document.getElementById("updatestoreCap");
            // modalBox.inputExist = document.getElementById("updatestoreExist");

            modalBox.inputId1.value=store.showstoreId;
            modalBox.inputId2.value=store.showstoreId;
            modalBox.inputName.value=store.showstoreName;
            modalBox.inputType.value=store.showstoreType;
            modalBox.inputLoca.value=store.showstoreLoca;
            modalBox.inputCap.value=store.showstoreCap;
            // modalBox.inputExist.value=store.showstoreExist;

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


//批量导入
// function batchImport(){

    // // 使用Ajax实现文件上传操作
    // // 创建一个FormData对象，用于存放上传图片的数据
    // var form_data = new FormData();
    // // 读取上传图片的数据
    // var file_info = $("#batchImport")[0].files[0];
    // // 将读取到的二进制数据添加到formData对象中
    // form_data.append("file", file_info);
    // // 使用Ajax发送异步请求并携带请求数据
    // $.ajax({
    //     async: true,
    //     url: "#",
    //     type: "post",
    //     headers: {"X-CSRFToken":$.cookie("csrftoken")},
    //     data: form_data,
    //     processData: false,
    //     contentType: false,
    //     success: function(data){
    //         alert("上传成功！");
    //     }
    // });
    // print("js jump success")
    // $("#batchImport").change(function(){
    //     // 使用Ajax实现文件上传操作
    //     // 创建一个FormData对象，用于存放上传图片的数据
    //     var form_data = new FormData();
    //     // 读取上传图片的数据
    //     var file_info = $("#batchImport")[0].files[0];
    //     // 将读取到的二进制数据添加到formData对象中
    //     form_data.append("file", file_info);
    //     // 使用Ajax发送异步请求并携带请求数据
    //     $.ajax({
    //         async: true,
    //         url: "/app/importStore/import/",
    //         type: "post",
    //         headers: {"X-CSRFToken":$.cookie("csrftoken")},
    //         data: form_data,
    //         processData: false,
    //         contentType: false,
    //         success: function(data){
    //             alert(data);
                // 获取图片元素修改其src属性值
                // $("#photo").attr("src", data);
                // // 分割用户头像的url地址
                // var photoname = data.split("/")[3];
                // // 将用户头像图片名称添加到隐藏域组件中
                // $("#photoname").attr("value", photoname);
//             }
//         });
//     });

// }