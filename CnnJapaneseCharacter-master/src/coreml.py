import coremltools

output_labels = [
'あ', 'い', 'う', 'え', 'お',
'か', 'き', 'く', 'け', 'こ',
'さ', 'し', 'す', 'せ', 'そ',
'た', 'ち', 'つ', 'て', 'と',
'な', 'に', 'ぬ', 'ね', 'の',
'は', 'ひ', 'ふ', 'へ', 'ほ',
'ま', 'み', 'む', 'め', 'も',
'や', 'ゆ', 'よ',
'ら', 'り', 'る', 'れ', 'ろ',
'わ', 'を', 'ん',
'が', 'ぎ', 'ぐ', 'げ', 'ご',
'ざ', 'じ', 'ず', 'ぜ', 'ぞ',
'だ', 'ぢ', 'づ', 'で', 'ど',
'ば', 'び', 'ぶ', 'べ', 'ぼ',
'ぱ', 'ぴ', 'ぷ', 'ぺ', 'ぽ']

scale = 1/255.

coreml_model = coremltools.converters.keras.convert('./hiraganaModel.h5',
                                                    input_names='image',
                                                    image_input_names='image',
                                                    output_names='output',
                                                    class_labels= output_labels,
                                                    image_scale=scale)
coreml_model.author = 'Melody Yang & Kaichi Momose'
coreml_model.license = 'MIT'
coreml_model.short_description = 'Detect hiragana from handwriting'
coreml_model.input_description['image'] = 'Grayscale image contains a handwritten letter'
coreml_model.output_description['output'] = 'Output a letter in hiragana'
coreml_model.save('hiraganaModel.mlmodel')
