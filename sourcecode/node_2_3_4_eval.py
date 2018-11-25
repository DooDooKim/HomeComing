#�̹��� evaluation ����

import time
import tensorflow as tf
import os

imagePath = '/home/pi/Desktop/pj/image1.jpg'                           
modelFullPath = '/home/pi/Desktop/pj/retrained_graph.pb'
labelsFullPath = '/home/pi/Desktop/pj/retrained_labels.txt'                                 
#Ʈ���̴� ��Ų �𵨰� label���� �ҷ��´�.
def create_graph():

    with tf.gfile.FastGFile(modelFullPath, 'rb') as f:

        graph_def = tf.GraphDef()

        graph_def.ParseFromString(f.read())

        _ = tf.import_graph_def(graph_def, name='')


def run_inference_on_image():

    answer = None


    if not tf.gfile.Exists(imagePath):

        tf.logging.fatal('File does not exist %s', imagePath)

        return answer

    image_data = tf.gfile.FastGFile(imagePath, 'rb').read()

    create_graph()


    with tf.Session() as sess:

        softmax_tensor = sess.graph.get_tensor_by_name('final_result:0')

        predictions = sess.run(softmax_tensor,

                               {'DecodeJpeg/contents:0': image_data})

        predictions = np.squeeze(predictions)



        top_k = predictions.argsort()[-1:][::-1]  # ���� ���� Ȯ���� ���� 1��(top 1)�� ������(predictions)�� ��´�.

        f = open(labelsFullPath, 'rb')

        lines = f.readlines()
        labels = [str(w).replace("", "") for w in lines]

        for node_id in top_k:

            human_string = labels[node_id]

            score = predictions[node_id]

        ans = labels[top_k[0]]
        answer = ans[2:-3]
        pb = predictions[top_k[0]]
        print(answer,'\t',pb)
        with open("/home/pi/Desktop/pj/eval1.txt","w") as f:
            f.write(answer)
        return ans
	# ���� Accuracy�� �������� eval%.txt�� �����Ѵ�.

if __name__ == '__main__':
    run_inference_on_image()