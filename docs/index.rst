.. FOR-FUN documentation master file, created by
   sphinx-quickstart on Jul 19 2020.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to FOR-FUN's documentation!
===================================

`FOR FUN <for-fun.readthedocs.io>`_

Different topics that I am learning in my part-time, just for fun!

Many parts are written in Chinese, as it is hard for me to translate some of the terminology.
Lots of content is very subjective, please understand.


Enjoy!

.. https://developer.adobe.com/document-services/apis/pdf-embed/

..
    <div id="adobe-dc-view" style="height: 360px; width: 700px;"></div>
    <script src="https://documentcloud.adobe.com/view-sdk/viewer.js"></script>
    <script type="text/javascript">
      document.addEventListener("adobe_dc_view_sdk.ready", function(){
        var adobeDCView = new AdobeDC.View({clientId: "<YOUR_CLIENT_ID>", divId: "adobe-dc-view"});
        adobeDCView.previewFile({
          content:{ location:
            { url: "https://gitee.com/gggliuye/pdfs_lib/raw/master/philosophy/dengxiaomang_critique_pure_reason.pdf"}},
          metaData:{fileName: "dengxiaomang Critique pure reason.pdf"}
        },
        {
          embedMode: "SIZED_CONTAINER"
        });
      });
    </script>


.. toctree::
   :maxdepth: 3
   :caption: Contents:

   Eastern/Index
   Western/Index
   Bio/Index
   Math/Index

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

My other documents
=========================

* `Mine homepage <https://gggliuye.github.io/>`_
* `Convex Optimization <https://cvx-learning.readthedocs.io/>`_
* `Computer Vision <https://vio.readthedocs.io/>`_
