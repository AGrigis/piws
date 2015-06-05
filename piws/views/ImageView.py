
# Cubicweb import
from cubicweb.view import View


# imports
from cubicweb.web.views.ajaxcontroller import ajaxfunc

from PIL import Image
import base64

try:
    import nibabel
except:
    print "Can't import Nibabel, visualisation module disabled"


class ImageView(View):
    """ Create a visualisation of a nifti file.
    """
    __regid__ = "scan_visu"
    paginable = False
    div_id = "scan_visu_id"

    def call(self, filepath):

        html = ""

        images = get_slices_from_nifti_2(filepath)

        test = images["coronal"][0]
        img = Image.fromarray(test)
        simg = base64.b64encode(img.tostring())
        print simg
        html = '<img src="data:image/png;base64,{0}"/>'.format(simg)

#        html = ""
#
#
#         # > begin the script
#        html = "<script type='text/javascript'> "
#        html += "$(document).ready(function() {"
#
#        # > create the table
#        html += "var table = $('#the_table').dataTable( { "
#
#        # > set table display options
#        html += "'scrollX': '100%',"
#        html += "'scrollY': '600px',"
#        html += "'scrollCollapse': true,"
#        html += "'sPaginationType': 'bootstrap',"
#        html += "'dom': 'T<\"clear\">lfrtip',"
#        html += "'lengthMenu': [ [10, 25, 50, 100, -1], [10, 25, 50, 100, 'All'] ],"
#        html += "'sServerMethod': 'POST',"
#        html += "'oLanguage': {'sSearch': 'ID'},"
#        html += "'pagingType': 'full_numbers',"
#        html += "'bProcessing': true,"
#
#
#        # > set table header
##        html += "'aoColumns': {0},".format(json.dumps(["1", "2"]))
#
#
#        # > set the ajax callback to fill dynamically the table
#        html += "'sAjaxSource': '{0}ajax?fname=get_slices_from_nifti',".format(self._cw.base_url())
#        html += "'fnServerParams': function (aoData) {"
#        html += "aoData.push("
#        html += "{ name: 'filepath', "
#        html += "value: '{0}'".format(json.dumps(filepath))
#        html += "}, "
#
#        # > close push data
#        html += ");"
#
#        # > close function fnServerParams
#        html += "},"
#
#        # > close table
#        html += "} );"
#
#        # > close script
#        html += "} );"
#
#        # Close script div
#        html += "</script>"
#
#
#        # > display the table in the body
#        html += "<table id='the_table' class='cell-border display'>"
#        html += "<thead></thead>"
#        html += "<tbody></tbody>"
#        html += "</table>"


#        html += """
#            <table id="example" class="display" cellspacing="0" width="100%">'
#            <thead>
#                """
#        html += '<tr>'
#        html +="""
#                    <th>Visu</th>
#
#                </tr>
#                </thead>
#            </table>
#
#            <script type='text/javascript'>
#
#
#                $(document).ready(function() {
#                    $('#example').DataTable( {
#                        serverSide: true,
#                        scrollCollapse: true,
#                        ordering: false,
#                        searching: false,
#                        ajax: function ( data, callback, settings ) {
#                            var out = [];
#
#"""
## > execute the ajax callback
#        html += "var postData = {};"
#        html += "postData.filepath = '{0}';".format(filepath)
#        html += "postData.index = {0};".format(100)
#        html += "postData.start = data.start;"
#        html += "postData.length = data.length;"
#
#        html += "var post = $.ajax({"
#
#        html += "url: '{0}ajax?fname=get_slices_from_nifti',".format(self._cw.base_url())
#        html += "type: 'POST',"
#        html += "data: postData"
#
#        html += "});"
#
#        # > the ajax callback is done, get the result set
#        html += "post.done(function(p){"
#
#        html += "var img_data_list = p.pix_values;"
#        html += "var dimx = {0};".format(nifti_width)
#        html += "var dimy = {0};".format(nifti_height)
#
#        html += "var balise_list = [];"
#
#        html += "for (var k = 0; k < img_data_list.length; k+=1){"
#
#        html += "var img_data = img_data_list[k];"
#        html += "var canvas = document.createElement('canvas');"
#        html += "var ctx = canvas.getContext('2d');"
#        # size the canvas to your desired image
#        html += 'canvas.width = dimx;'
#        html += 'canvas.height = dimy;'
#        # get the imageData and pixel array from the canvas
#        html += 'var imgData = ctx.getImageData(0, 0, dimx, dimy);'
#        html += 'var pixels = imgData.data;'
#        # manipulate some pixel elements
#
#        html += 'for (var i = 0; i < pixels.length; i += 4) {'
#
#        html += '    pixels[i] = img_data[i];'
#        html += '    pixels[i + 1] = img_data[i];'
#        html += '    pixels[i + 2] = img_data[i];'
#        html += '    pixels[i + 3] = 255;'
#        html += '}'
#        # put the modified pixels back on the canvas
#        html += 'ctx.putImageData(imgData, 0, 0);'
#        # create a new img object
#        html += 'var picture = new Image();'
#        # set the img.src to the canvas data url
#        html += 'picture.src = canvas.toDataURL();'
#
#        html +="""
#
#        var balise = "<img src=" + picture.src +">"
#        balise_list.push(balise)
#        }
#
#        for ( var i=0, ien=balise_list.length ; i<ien ; i++ ) {
#                out.push( [balise_list[i]] );
#            }
#
#            setTimeout( function () {
#                callback( {
#                    draw: data.draw,
#                    data: out,
#                """
#        html += 'recordsTotal: {0},'.format(nifti_depth)
#        html += 'recordsFiltered: {0}'.format(nifti_depth)
#        html +="""
#                } );
#            }, 50 );})
#        },
#        dom: "rtiS",
#        scrollY: 1000,
#        scroller: {
#            loadingIndicator: true,
#                """
#        html += 'rowHeight: {0}'.format(nifti_height)
#        html +="""
#        }
#    } );
#} );
#
#
#</script>
#            """

        self.w(u'{0}'.format(html))


@ajaxfunc(output_type="json")
def get_slices_from_nifti(self):
    """
    Function that will read the nifti files and create a list of images to
    display
    """
    nifti_path = self._cw.form["filepath"]
    index_input = int(self._cw.form['iDisplayStart'])
    index_stop = int(self._cw.form['iDisplayLength'])
    # load nift
#    print self._cw.form['iDisplayStart']
#    print self._cw.form['iDisplayLength']
    nifti = nibabel.load(nifti_path)

    volumes = nifti.get_data()
    out_val_list = []
    # TODO  3D or 4D volume
    for index in range(index_input, index_input + index_stop - 1):
        _nif_img = volumes[:, :, index]

        list_nif_img = _nif_img.tolist()
        list_of_values = []
        for row_index in range(len(list_nif_img[0])):
            for col_index in reversed(range(len(list_nif_img))):
                list_of_values.append(list_nif_img[col_index][row_index])

        out_val = []
        for item in reversed(list_of_values):
            out_val.append(item)
            out_val.append(item)
            out_val.append(item)
            out_val.append(item)

        out_val_list.append(out_val)

    out = {"dim_x": nifti.shape[0],
           "dim_y": nifti.shape[1],
           "pix_values": out_val_list}
    return out


def get_slices_from_nifti_2(nifti_path):
    """
    Function that will read the nifti files and create a list of images to
    display
    output: {coronal mid-slice: {coronal slices}, sagital mid-slices: {...}}
    """
    # load nift
    nifti = nibabel.load(nifti_path)
    out = {}
    volumes = nifti.get_data()

    # TODO  3D or 4D volume

    for j, key in zip(range(3), ["axial", "coronal", "sagittal"]):

        out_val = []

        for index in range(nifti.shape[j] - 1):
            if j == 0:
                _nif_img = volumes[index, :, :]
            elif j == 1:
                _nif_img = volumes[:, index, :]
            else:
                _nif_img = volumes[:, :, index]

            out_val.append(_nif_img)

            if index == round(nifti.shape[j] / 2, 0):
                mid_slices = _nif_img

        out[key] = [mid_slices, out_val]
    return out


def get_nifti_dim_from_nifti(nifti_path):
    """
    Function that will read the nifti files and create a list of images to
    display
    """
    # load nifti
    nifti = nibabel.load(nifti_path)

    volume = nifti.get_data()
    # TODO 3D or 4D volume
    return volume.shape


def registration_callback(vreg):
    vreg.register(get_slices_from_nifti)
    vreg.register(ImageView)
