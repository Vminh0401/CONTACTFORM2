from django.shortcuts import render
from django.core.mail import send_mail


def index(request):
    if request.method == "POST":
        # name = request.POST.get('full-name')
        # email = request.POST.get('email')
        # subject = request.POST.get('subject')
        # message = request.POST.get('message')

        name = request.POST.get('cs1Name')
        email = request.POST.get('cs1Email')
        select = request.POST.get('form-select')
        phone = request.POST.get('cs1PhoneNum')
        thanks = f'Kính gửi Quý khách hàng,\n\nLời đầu tiên xin được thay mặt toàn bộ đội ngũ nhân viên gửi lời cảm ơn chân thành và sâu sắc nhất tới Quý khách hàng đã tin tưởng đồng hành, hợp tác cũng như ủng hộ giupviechn.vn\n\nChính những sự yêu mến và niềm tin của Quý khách hàng là niềm tự hào và thành công lớn nhất của chúng tôi, đồng thời cũng là động lực để chúng tôi tiếp tục phát triển trong tương lai. \n\n Hy vọng trong thời gian sắp tới, mối quan hệ của hai bên càng lúc càng bên chặt. Chúng tôi sẽ không ngừng phát triển, nâng cao chất lượng dịch vụ để có thể phục vụ Quý khách hàng tốt hơn. \n\nMột lần nữa, chúng tôi xin gửi lời cảm ơn chân thành và sự tri ân sâu sắc tới Quý khách hàng. Xin chúc bạn sức khỏe luôn dồi dào, hạnh phục và thành công. \n\nTrân Trọng! \n\nhttp://giupviechn.vn/'
        # link = ('http://giupviechn.vn/')

        data = {
            # 'name': name,
            # 'email': email,
            # 'subject': subject,
            # 'message': message

            'name': name,
            'email': email,
            'select': select,
            'phone': phone,
            'thanks': thanks
        }

        customer_name = data.get('name')
        customer_email = data.get('email')
        customer_select = data.get('select')
        customer_phone = data.get('phone')

        message = '''
        New message: {}

        From: {}
        '''.format(data['phone'], data['email'])
        send_mail(data['select'], thanks, '', [email])
        return render(request, template_name='infor/thanks.html')
    return render(request, 'infor/index.html', {})

