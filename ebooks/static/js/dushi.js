$(function () {
    var oExports = {
        initialize: fInitialize,
        // 渲染更多数据
        renderMore: fRenderMore,
        // 请求数据
        requestData: fRequestData,
        // 简单的模板替换
        tpl: fTpl
    };
    // 初始化页面脚本
    oExports.initialize();

    function fInitialize() {

        var that = this;
        // 常用元素
        that.listEl = $('div.listmore');
        // 初始化数据

        that.page = 1;
        that.pageSize = 12;
        that.listHasNext = true;
        // 绑定事件
        $('#loadmore').on('click', function (oEvent) {
            console.log("bihao")
            var oEl = $(oEvent.currentTarget);
            var sAttName = 'data-load';
            // 正在请求数据中，忽略点击事件
            if (oEl.attr(sAttName) === '1') {
                return;
            }
            // 增加标记，避免请求过程中的频繁点击
            oEl.attr(sAttName, '1');
            that.renderMore(function () {
                // 取消点击标记位，可以进行下一次加载
                oEl.removeAttr(sAttName);
                // 没有数据隐藏加载更多按钮
                !that.listHasNext && oEl.hide();
            });
        });
    }

    function fRenderMore(fCb) {
        var that = this;
        // 没有更多数据，不处理
        if (!that.listHasNext) {
            return;
        }
        that.requestData({

            page: that.page + 1,
            pageSize: that.pageSize,
            call: function (oResult) {
                console.log(oResult)
                // 是否有更多数据
                that.listHasNext = !!oResult.has_next && (oResult.yanqing || []).length > 0;
                // 更新当前页面
                that.page++;
                // 渲染数据
                var sHtml = '<div id="container" role="main"><div id="boxes" class="masonry" style="position: relative; height: 1890px;">';


                $.each(oResult.yanqing, function (nIndex, oImage) {

                    var title = oImage["title"]
                    var img =oImage["img"]
                    var cate =oImage["cate"]
                    var author =oImage["author"]
                    var size = oImage["size"]
                    var date = oImage["date"]
                    var down =oImage["down"]
                    var listT =oImage["listT"]
                    var listL =oImage["listL"]
                    var listH =oImage["listH"]
                    sHtml += that.tpl([
'<div class="box masonry-brick" style="position: absolute; top: #{listT}px; left: #{listL}px;">',
		'<div class="rel">',
			'<a href="#"><img width="220" height="#{listH}" src="#{img}" class="attachment-homepage-thumb wp-post-image" alt="" title=""></a>',
			'<h1><a href="#">#{title}</a></h1>',
			'<div class="post-date">#{cate}</div>',
			'<div class="post-date">#{author}</div>',
			'<div class="post-date">#{size}</div>',
			'<div class="post-date">#{date}</div>',

		'<p>#{content}</p>',
'<div class="readmore"><a href="#{down}">立即下载 →</a></div>',

		'</div>',
	'</div>',

                        ].join(''), oImage);
                });
                sHtml+='</div></div>'
                sHtml && that.listEl.append(sHtml);
            },
            error: function () {
                alert('出现错误，请稍后重试');
            },
            always: fCb
        });
    }

    function fRequestData(oConf) {
        var that = this;
        var sUrl = '/dushi_api/'+oConf.page + '/' + oConf.pageSize + '/';
        console.log(sUrl)
        $.ajax({url: sUrl, dataType: 'json'}).done(oConf.call).fail(oConf.error).always(oConf.always);
    }

    function fTpl(sTpl, oData) {
        var that = this;
        sTpl = $.trim(sTpl);
        return sTpl.replace(/#{(.*?)}/g, function (sStr, sName) {
            return oData[sName] === undefined || oData[sName] === null ? '' : oData[sName];
        });
    }
});