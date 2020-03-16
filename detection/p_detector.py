import tensorflow as tf
import sys
import train.config as config

class PDetector:
	def __init__(self,model_path):
		graph = tf.Graph()
		with graph.as_default():
			self.image_op = tf.placeholder(tf.float32,name='image')
			self.width_op = tf.placeholder(tf.int32,name='image_width')
			self.height_op = tf.placeholder(tf.int32,name='image_height')
			image_reshape = tf.reshape(self.image_op,[1,self.height_op,self.width,3])

			self.sess = tf.Session()

			saver = tf.train.Saver()
			model_file = tf.train.latest_checkpoint(moedl_path)
			saver.restore(self.sess,model_file)

				

